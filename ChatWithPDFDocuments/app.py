import streamlit as st
from streamlit_chat import message
from utils import *
import json
from dotenv import load_dotenv
from pathlib import Path

base_path=Path(__file__.rsplit('\\', 1)[0])
load_dotenv(base_path.parent / '.env')

def init_var_session_state(var, value):
    if var not in st.session_state:
        st.session_state[var] = value

vars_to_init = [
    ("generated", []),
    ("past", []),
    ('btn_create_index', False),
    ('available_index', (base_path / 'faiss_index').is_dir()),
    ('len_pdfs', 0),
    ('available_index_block', True)
]

for v in vars_to_init: init_var_session_state(*v)


def func_btn_use_index():
    st.session_state.btn_create_index = False
    st.session_state.len_pdfs = 1
    st.session_state.available_index_block = False


def func_btn_remove_index():
    delete_index()
    st.session_state.btn_create_index = False
    st.session_state.len_pdfs = 0
    st.session_state.available_index_block = False

def func_reset_conv():
    st.session_state["generated"] = []
    st.session_state["past"] = []

def func_save_conv():
    conv = {}
    print('save')
    for i in range(len(st.session_state["generated"])):
        conv['user'] = st.session_state["past"][i]
        conv['assistant'] = st.session_state["generated"][i]
    with (base_path / 'conversation.json').open('w') as f:
        json.dump(conv, f, indent=4)


def main():
    st.set_page_config(page_title="Chat with your Documents (PDF)")
    st.header("Chat with your Documents (PDF)")

    with st.sidebar:
        st.subheader('Create your index from PDF')
        pdfs = st.file_uploader('Select PDF files!', type='pdf', accept_multiple_files=True)

        if st.button('Create Index!', use_container_width=True) \
            and len(pdfs) != 0:
            delete_index()
            st.session_state.btn_create_index = True
            st.session_state.len_pdfs = len(pdfs)

        save_conv = st.button("Save Converstation!", use_container_width=True)
        if save_conv: func_save_conv()

        reset_conv = st.button("Reset Converstation!", use_container_width=True)
        if reset_conv: func_reset_conv()



    if st.session_state.available_index_block:
        if st.session_state.available_index:
            st.success('An index was found, would you like to use it?')
            col1, col2 = st.columns([1.5,8.5])
            with col1:
                st.button('Use it!', use_container_width=True, on_click=func_btn_use_index)
            with col2:
                st.button('Overwrite it!', on_click=func_btn_remove_index)


    embedding = get_embedding_model()

    if st.session_state.btn_create_index:
        if st.session_state.len_pdfs == 0: return
        func_reset_conv()
        text = pdf_to_text(pdfs)
        chunks = split_text(text)
        db = create_vector_db(chunks, embedding)
        st.session_state.btn_create_index = False
        st.session_state.available_index = (base_path / 'faiss_index').is_dir()
        print('@create new db')

    if st.session_state.available_index:
        db = load_index(embedding)

    retriever = db.as_retriever(search_kwargs={'k':3})

    llm = get_llm()
    memory = get_memory()
    prompt = get_prompt_template()

    chain = get_chain(llm, retriever, memory, prompt)


    user_input = st.chat_input(placeholder="What would you like to ask?")

    if user_input:
        output = chain.run(question=user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)

    if st.session_state["generated"]:
        for i in range(len(st.session_state["generated"])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
            message(st.session_state["generated"][i], key=str(i))


if __name__ == '__main__':
    main()

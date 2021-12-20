import streamlit as st


def main():
    st.title('제목을 입력해주세요')
    st.text('텍스트를 입력해주세요')
    st.header('헤더를 입력해주세요')
    st.subheader('서브헤더를 입력해주세요')

    st.markdown('#큰글자')
    st.markdown('##중간글자')
    st.markdown('###이것응ㄴ 무슨 글자?')

    st.success('성공했을 때~')
    st.warning('경고를 하고 싶을 때~')
    st.info('인포를 주고 싶을때')
    st.error('에러가 발생했음을 알리고 싶을때')
    st.exception('예외 상황이 발생했을 때')


if __name__ == '__main__':
    main()


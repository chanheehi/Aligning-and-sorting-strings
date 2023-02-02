# 함수 생성
def wc_rjust(text, length, padding=' '):    # 우측정렬
    return padding * (length - len(text)) + text

def wc_ljust(text, length, padding=' '):    # 좌측정렬
    return text + (padding * (length - len(text)))

def wc_center(text, length, padding=' '):   # 중앙정렬
    margin = int((length - len(text))/2)
    i = 0
    if length % 2 == 1: # length가 홀수일 경우
        if length == len(text):    # length와 text의 길이가 같을 경우
            return (padding * margin) + text + (padding * margin)
        i = i+1 # length가 홀수일 경우 공백 1개를 뒤에 추가
        if len(text) % 2 == 1: # text의 길이가 홀수일 경우
            i = i-1 # text의 길이가 홀수일 경우 공백 1개를 삭제
        return (padding * margin) + text + (padding * (margin + i)) # 홀수일 경우 공백 i개를 뒤에 추가
        # return (padding * (margin + i)) + text + (padding * margin) # 홀수일 경우 공백 i개를 앞에 추가
    return (padding * margin) + text + (padding * margin)

text = '123456'
length = 10
# 함수 활용
print('우측정렬 :' + wc_rjust(text, length) + ':끝')
print('중앙정렬 :' + wc_center(text, length) + ':끝')
print('좌측정렬 :' + wc_ljust(text, length) + ':끝')
import random
import os
import sys
import platform
import time
from collections import namedtuple

FILE_PATH = "./words.txt"
Entry = namedtuple("Entry", ["abbreviation", "english"])


def insert(entries):
    while True:
        abbreviation = input("영단어(Full Name)를 입력하세요(#: 이전단계로): ").strip()
        if abbreviation == "#":
            return
        english = input("약어를 입력하세요: ").strip()
        if english == "#":
            return
        entries.append(Entry(abbreviation, english))


# TODO: 오답노트 만들기 
# def wrong_ans_note(entries):
#     while True:
#         abbreviation = input("영단어(Full Name)를 입력하세요(#: 이전단계로): ").strip()
#         if abbreviation == "#":
#             return
#         english = input("약어를 입력하세요: ").strip()
#         if english == "#":
#             return
#         entries.append(Entry(abbreviation, english))


def query(entries):
    total, right = 0, 0
    while True:
        word_pair = random.choice(entries)
        abbreviation = input(f"다음 약어에 해당하는 단어는? {word_pair.english}:").lower()

        if abbreviation == "#":
            percentage = (right * 100) / total
            print(f"전체 {right} 문제 중 {total} 문제를 맞추었습니다.")
            print(f"성취도: {percentage} % / 100%")
            input("이전 단계로 돌아가려면 아무키나 입력하세요...")
            return
        total += 1
        if abbreviation.strip() == word_pair.abbreviation.lower():
            print("정답입니다.")
            right += 1
        else:
            print("틀렸습니다!")
            print(f"정답은 {word_pair.abbreviation} 였습니다.")


def printall(entries):
    if len(entries) == 0:
        print("아무런 단어가 없습니다.")
        input("이전 단계로 돌아가려면 아무키나 입력하세요...")
        return
    for word_pair in entries:
        print("{} : {}".format(*word_pair))
        
    input("이전 단계로 돌아가려면 아무키나 입력하세요...")


def backup_wordpairs(entries, file_path):
    with open(file_path, 'w') as words:
        for word_pair in entries:
            words.write("{},{}\n".format(*word_pair))


def clear_screen():
    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def main(file_path=FILE_PATH):
    if os.path.isfile(file_path):
        with open(file_path) as words:
            entries = [Entry(*map(str.strip, line.split(",")))
                       for line in words]
    else:
        clear_screen()
        print("단어사전이 없습니다. 새로 하나 만들어야 합니다.")
        question_newfile = input("하나 만드시겠습니까?(y/n)")
        if question_newfile == "y":
            newfile = open(FILE_PATH, "w")
            newfile.close()
            print("생성되었습니다. 프로그램을 다시 실행시켜주세요.")
            sys.exit()
        else:
            print("단어사전이 없기 때문에 종료합니다.")
            sys.exit()

    while True:
        clear_screen()
        print("1. 새로운 단어 추가")
        print("2. 단어 연습하기")
        print("3. 단어 리스트 보기")
        print("4. 끝내기")
        print("5. 저장된 단어 모두 삭제하기")
        command = input("명령을 입력하세요: ")

        if command == "1":
            clear_screen()
            insert(entries)
            backup_wordpairs(entries, file_path)
        elif command == "2":
            clear_screen()
            query(entries)
        elif command == "3":
            printall(entries)
        elif command == "4":
            clear_screen()
            break
        elif command == "5":
            clear_screen()
            print("정말 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다.")
            print("정말 삭제하고자 한다면 다음을 입력하세요.")
            print("I don't care i lost my dictionary.")
            remove_prompt = input()
            if remove_prompt =="I don't care i lost my dictionary.":
                entries.clear()
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print("삭제되었습니다. 다시 실행시켜주세요.")
                    sys.exit()
            else:
                continue
        else:
            clear_screen()
            print("알 수 없는 선택입니다. 다시 고르세요.")

    print(" ------- 단어 시험 프로그램이 종료됩니다. ----------  ")
    sys.exit()

if __name__ == "__main__":
    main()
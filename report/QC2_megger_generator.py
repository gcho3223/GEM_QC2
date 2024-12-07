import os
from pathlib import Path
import shutil

def main(date_input):
    # 해당 날짜의 디렉토리로 이동 및 'megger' 디렉토리 생성
    base_dir = Path(f"./QC2_results/data_ME0_foils_{date_input}")
    megger_dir = base_dir / "megger"
    megger_dir.mkdir(parents=True, exist_ok=True)
    print(f"'megger' directory has been created: {megger_dir}")
    # 3. QC2LONG_PART1으로 시작하는 파일 찾기
    original_files = list(base_dir.glob("QC2LONG_PART1*.txt"))
    # 4. megger 디렉토리에 파일 생성 및 데이터 입력
    for original_file in original_files:
        new_filename = original_file.name.replace("QC2LONG_PART1", "QC2FAST")
        new_file_path = megger_dir / new_filename
        try:
            data_correct = False
            while not data_correct:
                with open(new_file_path, 'w') as new_file:
                    # 헤더 작성
                    new_file.write("Time (minutes)\tImpedance (GOhm)\tSparks\n")
                    print("start entering the QC2FAST data for the file: ", new_filename)
                    # 데이터 입력
                    data = {}
                    for time in [0.5, 1, 2, 3, 4, 5]:
                        impedance, sparks = input(f"Imp Spark @ {time} min: ").split()
                        data[time] = (impedance, sparks)
                        new_file.write(f"{time}\t{impedance}\t{sparks}\n")
                
                # 파일 내용 출력 및 사용자 확인 반복
                while True:
                    with open(new_file_path, 'r') as new_file:
                        print("\nFile content:")
                        print(new_file.read())
                    
                    correct = input("Is the content correct? (y/n): ").strip().lower()
                    if correct == 'y':
                        data_correct = True
                        break
                    else:
                        # 틀린 시간대 입력받기
                        wrong_time = float(input("Enter the wrong time: "))
                        impedance, sparks = input(f"Imp Spark @ {wrong_time} min: ").split()
                        data[wrong_time] = (impedance, sparks)
                        # 파일 업데이트
                        with open(new_file_path, 'w') as new_file:
                            new_file.write("Time (minutes)\tImpedance (GOhm)\tSparks\n")
                            for time in [0.5, 1, 2, 3, 4, 5]:
                                impedance, sparks = data[time]
                                new_file.write(f"{time}\t{impedance}\t{sparks}\n")
            print(f"file has been created: {new_file_path}")
        except Exception as e:
            print(f"error occurred while processing the file: {e}")
if __name__ == "__main__":
    import sys
    date_input = sys.argv[1]  # 명령줄 인자로 date_input 받기
    main(date_input)

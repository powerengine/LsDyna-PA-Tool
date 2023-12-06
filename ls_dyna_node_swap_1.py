# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 22:23:12 2023

@author: USER
"""

import pandas as pd


##########################################################################
#  Update 할 Node 가 있는 파일 Open
##########################################################################

file_path = 'section_shell_hourglassing_updated.key'  # 파일 경로

update_nodes_data = []  # 노드 데이터를 저장할 리스트

# 파일 열기
with open(file_path, 'r') as file:
    found_node_data = False
    skip_lines = False
    
    for line in file:
        # 공백이거나 빈 행인 경우 무시
        if found_node_data and not line.strip():  
            continue
        
        if found_node_data and not line.startswith('$') and not line.startswith('*'):  # $로 시작하는 행은 무시
            # 예시: 노드 데이터의 구분자가 공백이라고 가정
            node_info = line.split()  # 데이터를 분리하여 리스트로 저장
            update_nodes_data.append(node_info)  # 추출된 노드 데이터를 리스트에 추가
        elif line.startswith('*NODE'):  # *NODE 행을 찾으면 데이터 추출 시작
            found_node_data = True
        elif found_node_data and line.startswith('*'):  # 다른 *로 시작하는 행을 만나면 추출 종료
            found_node_data = False

# 데이터프레임 생성
df_nodes_update = pd.DataFrame(update_nodes_data, columns=['Node_ID', 'X', 'Y', 'Z', 'tc', 'rc'])  # 예시: 노드 ID, X, Y, Z 좌표
print(df_nodes_update.head())  # 데이터프레임 확인
############################################################################


############################################################################
#                         수정할 파일 Open
############################################################################

file_path = 'section_shell_hourglassing.key'  # 파일 경로

nodes_data = []  # 노드 데이터를 저장할 리스트

# 파일 열기
with open(file_path, 'r') as file:
    found_node_data = False
    skip_lines = False
    
    for line in file:
        
        # 공백이거나 빈 행인 경우 무시
        if found_node_data and not line.strip():  
            continue
        
        if found_node_data and not line.startswith('$') and not line.startswith('*'):  # $로 시작하는 행은 무시
            # 예시: 노드 데이터의 구분자가 공백이라고 가정
            node_info = line.split()  # 데이터를 분리하여 리스트로 저장
            node_number=node_info[0]
         
            #nodes_data.append(node_info)  # 추출된 노드 데이터를 리스트에 추가
        elif line.startswith('*NODE'):  # *NODE 행을 찾으면 데이터 추출 시작
            found_node_data = True
        elif found_node_data and line.startswith('*'):  # 다른 *로 시작하는 행을 만나면 추출 종료
            found_node_data = False



############################################################################
#                 파일 수정을 위한 영역
############################################################################

# section_shell_hourglassing.key 파일 업데이트를 위한 함수
def update_file(file_path, node_number, new_content):
    updated_lines = []  # 새로운 파일 내용을 저장할 리스트

    with open(file_path, 'r') as file:
        lines = file.readlines()

        found_node_data = False
        found_target_node = False

        for line in lines:
            if found_node_data and not line.strip():
                continue

            if found_node_data and not line.startswith('$') and not line.startswith('*'):
                node_info = line.split()
                if node_info[0] == node_number:  # 노드 번호가 일치하면 새로운 내용으로 변경
                    line = ' '.join(new_content) + '\n'
                    found_target_node = True

            elif line.startswith('*NODE'):
                found_node_data = True
                found_target_node = False

            elif found_node_data and line.startswith('*'):
                found_node_data = False

            updated_lines.append(line)

    if found_target_node:
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)
        print(f"Node {node_number} updated in file: {file_path}")
    else:
        print(f"Node {node_number} not found in file: {file_path}")


# df_nodes_update의 Node_ID를 기반으로 section_shell_hourglassing.key 파일 업데이트
for node_number in df_nodes_update['Node_ID']:
    # df_nodes_update에 node_number가 있는지 확인하고, 있다면 그 행의 데이터를 가져옵니다.
    node_data = df_nodes_update[df_nodes_update['Node_ID'] == node_number].iloc[0]

    # section_shell_hourglassing.key 파일 업데이트
    update_file('section_shell_hourglassing.key', node_number, node_data)





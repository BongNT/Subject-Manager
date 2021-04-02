import os

if __name__ == '__main__':
    absFilePath = os.path.abspath(__file__)
    print(absFilePath)
    projectPath = absFilePath
    for i in range(3):
        projectPath = os.path.dirname(projectPath)
    print(projectPath)
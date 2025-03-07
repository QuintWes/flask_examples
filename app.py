import multiprocessing
import os

def run_main_app():
    os.system("python main_app.py")


def run_swagger_example():
    os.system("python flask_swagger_example.py")


def run_restx_example():
    os.system("python flask_restx_example.py")


# def run_apifairy_example():
#     os.system("python apifairy_example.py")


def run_connexion_example():
    os.system("python connexion_example.py")


if __name__ == '__main__':
    processes = [
        multiprocessing.Process(target=run_main_app),
        multiprocessing.Process(target=run_swagger_example),
        multiprocessing.Process(target=run_restx_example),
        # multiprocessing.Process(target=run_apifairy_example),
        multiprocessing.Process(target=run_connexion_example),
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

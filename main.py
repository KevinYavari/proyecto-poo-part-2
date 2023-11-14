import streamlit as st
from view import View
from model import model
from controller import controller

def main():
    controller_instance = controller()
    controller_instance.showmenu()

if __name__ == "__main__":
    main() 
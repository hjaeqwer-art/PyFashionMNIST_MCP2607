import streamlit as st
import torch
from torch import nn
import torchvision.transforms as transforms
import os, json

st.title('FashionMNSIST')

img_file = st.file_uploader('이미지를 업로드하세요', type=['png', 'jpg', 'jpeg'])

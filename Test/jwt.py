from crypt import methods
from flask import Flask, redirect, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient 


# JWT 토큰 SECRECT KEY를 사용하여 로그인 인증 인가 구현
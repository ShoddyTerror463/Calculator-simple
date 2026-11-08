from pyscript import when, display
from pyscript import document
import math


def inputFill(event):
    if document.querySelector('#answerInput').textContent == 'Input':
        document.querySelector('#answerInput').textContent = ''

    if event.target.id == '1':
        document.querySelector('#answerInput').textContent += '1'
    elif event.target.id == '2':
        document.querySelector('#answerInput').textContent += '2'
    elif event.target.id == '3':
        document.querySelector('#answerInput').textContent += '3'
    elif event.target.id == '4':
        document.querySelector('#answerInput').textContent += '4'
    elif event.target.id == '5':
        document.querySelector('#answerInput').textContent += '5'
    elif event.target.id == '6':
        document.querySelector('#answerInput').textContent += '6'
    elif event.target.id == '7':
        document.querySelector('#answerInput').textContent += '7'
    elif event.target.id == '8':
        document.querySelector('#answerInput').textContent += '8'
    elif event.target.id == '9':
        document.querySelector('#answerInput').textContent += '9'
    elif event.target.id == '0':
        document.querySelector('#answerInput').textContent += '0'
    elif event.target.id == 'plus':
        document.querySelector('#answerInput').textContent += '+'
    elif event.target.id == 'subtract':
        document.querySelector('#answerInput').textContent += '-' 
    elif event.target.id == 'decimal':
        document.querySelector('#answerInput').textContent += '.'   
    else:
        document.querySelector('#answerInput').textContent += 'Error'

def outputFill(event):
    if document.querySelector('#answerInput').textContent == 'Input':
        document.querySelector('#answerOutput').textContent == 'Please type in something'
    else:
        equation = document.querySelector('#answerInput').textContent
        try:
            answer = eval(equation)
            round(answer,5)
            document.querySelector('#answerOutput').textContent = answer
            pastCalculation1 = f"Input: {equation}"
            pastCalculation2 = f"Output: {answer}"
            document.querySelector('#pastCalcContainer').textContent += pastCalculation1 + ' ' + pastCalculation2 + '; '
        except:
            document.querySelector('#answerOutput').textContent = 'Syntax error'
        

def clear(event):
    document.querySelector('#answerInput').textContent = ''
    document.querySelector('#answerOutput').textContent = ''




      

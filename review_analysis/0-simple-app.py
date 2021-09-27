import justpy as jp 

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h1 text-right text-bold q-pa-sm")
    p1 = jp.QDiv(a=wp, text="There graphs represent course reviedw analysis", classes='q-mt-xl')
    return wp

jp.justpy(app)
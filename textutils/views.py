from django.http import HttpResponse
from django.shortcuts import render

def index (request):

    return render(request, 'textutils/index.html')

def analyze (request):
    # get the text entered by user
    djtext= request.POST.get('text', 'default')
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps= request.POST.get('fullcaps', 'off')
    newlineremover= request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')
    charcounter= request.POST.get('charcounter', 'off')

    # Check which checkbox is on
    if removepunc == "on":

        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # Analyze the text
        djtext= analyzed
        # return render(request,'analyze.html', params)

    if (fullcaps == "on"):

        analyzed =" "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!='\r':
                analyzed = analyzed + char
        # print("pre",analyzed)
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):

                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (charcounter == "on"):
        charcount = 0
        for char in djtext:
            charcount += 1
        cccc=(f"Number of characters in entered text is {charcount}")
        params = {'purpose': 'Character Counted', 'analyzed_text': cccc}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    return render(request, 'textutils/analyze.html', params)

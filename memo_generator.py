import tkinter as tk
import datetime
import ollama
from docx import Document
from docx2pdf import convert

def generate_memo():
    memo_topic = mtopic.get()
    sender = msender.get()
    receiver = mreceiver.get()
    subject = msubject.get()
    sender_name = sender_name_entry.get()
    today_date = datetime.date.today().strftime('%B %d, %Y')
    
    prompt = f"Write a three-paragraph memo about {memo_topic} which will be from {sender} ({sender_name}) to {receiver} with subject as '{subject}', and memo writting date as: {today_date}. Write {sender_name} as the Sender's name of my name.the instructions are : dont write any links or anything from otherthan i gave you context for "
    
    response = ollama.chat(model='tinyllama', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    
    memo_content = response['message']['content']
    
    # Load the template document
    template_path = 'memotemplate_template.docx'
    doc = Document(template_path)
    
    for paragraph in doc.paragraphs:
        if '[Memo_body]' in paragraph.text:
            paragraph.text = paragraph.text.replace('[Memo_body]', memo_content)

    output_path = 'memo.docx'
    doc.save(output_path)
    convert(output_path)
    
    status_label.config(text="Successfully generated. Check the document for your memo.")
    

# GUI setup
root = tk.Tk()
root.title("Memo Generator")
root.geometry("800x400")

# Memo generation section
mlabel = tk.Label(root, text="Memo Generation", font=('Helvetica', 16, 'bold'))
mlabel.pack(pady=10)

mtopic_label = tk.Label(root, text="Memo Topic:")
mtopic_label.pack(pady=5)
mtopic = tk.Entry(root, width=100)
mtopic.pack()

msender_label = tk.Label(root, text="Sender (email/ID):")
msender_label.pack(pady=5)
msender = tk.Entry(root, width=100)
msender.pack()

sender_name_label = tk.Label(root, text="Sender's Name:")
sender_name_label.pack(pady=5)
sender_name_entry = tk.Entry(root, width=100)
sender_name_entry.pack()

mreceiver_label = tk.Label(root, text="Receiver:")
mreceiver_label.pack(pady=5)
mreceiver = tk.Entry(root, width=100)
mreceiver.pack()

msubject_label = tk.Label(root, text="Subject:")
msubject_label.pack(pady=5)
msubject = tk.Entry(root, width=100)
msubject.pack()

generate_btn = tk.Button(root, text="Generate Memo", command=generate_memo)
generate_btn.pack(pady=10)

status_label = tk.Label(root, text="", fg="green", font=('Helvetica', 12))
status_label.pack(pady=10)

root.mainloop()

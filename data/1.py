import gradio as gr
import os
import time


# Chatbot demo with multimodal input (text, markdown, LaTeX, code blocks, image, audio, & video). Plus shows support for streaming text.


def print_like_dislike(x: gr.LikeData):
    print(x.index, x.value, x.liked)


def add_text(history, text):
    history = history + [(text, None)]
    return history, gr.Textbox(value="", interactive=False)


def bot(history):
    # response = "**That's cool!**"
    history[-1][1] = ("buck-boost.jfif",)
    return history

    # history[-1][1] = ""
    # for character in response:
    #     history[-1][1] += character
    #     time.sleep(0.05)
    #     yield history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(
        [],
        elem_id="chatbot",
        bubble_full_width=False,
        avatar_images=(None, (os.path.join(os.path.dirname(__file__), "avatar.png"))),
    )

    with gr.Row():
        txt = gr.Textbox(
            scale=4,
            show_label=False,
            placeholder="Enter text and press enter, or upload an image",
            container=False,
        )

    txt_msg = txt.submit(add_text, [chatbot, txt], [chatbot, txt], queue=False).then(
        bot, chatbot, chatbot, api_name="bot_response"
    )

    txt_msg.then(lambda: gr.Textbox(interactive=True), None, [txt], queue=False)

    chatbot.like(print_like_dislike, None, None)

demo.queue()
demo.launch()
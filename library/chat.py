import os

from transformers import PreTrainedModel, PreTrainedTokenizer

from .model import Model
from .templates import LLAMA_CHAT_TEMPLATE, MIXTRAL_INSTRUCT_TEMPLATE


class LlamaChat(Model):
    def __init__(self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer) -> None:
        super().__init__(model, tokenizer)
        self.template = LLAMA_CHAT_TEMPLATE


class MixtralInstruct(Model):
    def __init__(self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer) -> None:
        super().__init__(model, tokenizer)
        self.template = MIXTRAL_INSTRUCT_TEMPLATE


class Vicuna(Model):
    def __init__(self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer) -> None:
        super().__init__(model, tokenizer)
        template_path = os.path.join(
            os.path.dirname(__file__), "./templates_jinja/vicuna.jinja"
        )
        chat_template = open(template_path).read()
        chat_template = chat_template.replace("    ", "").replace("\n", "")
        self.template = chat_template


class ChatML(Model):
    def __init__(self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer) -> None:
        super().__init__(model, tokenizer)
        template_path = os.path.join(
            os.path.dirname(__file__), "./templates_jinja/chatml.jinja"
        )
        chat_template = open(template_path).read()
        chat_template = chat_template.replace("    ", "").replace("\n", "")
        self.template = chat_template


class DeepSeek(Model):
    def __init__(self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer) -> None:
        super().__init__(model, tokenizer)
        template_path = os.path.join(
            os.path.dirname(__file__), "./templates_jinja/deep_seek.jinja"
        )
        chat_template = open(template_path).read()
        chat_template = chat_template.replace("    ", "").replace("\n", "")
        self.template = chat_template


class MetaMath(Model):
    def __init__(self, model: PreTrainedModel, tokenizer: PreTrainedTokenizer) -> None:
        super().__init__(model, tokenizer)
        template_path = os.path.join(
            os.path.dirname(__file__), "./templates_jinja/alpaca.jinja"
        )
        chat_template = open(template_path).read()
        chat_template = chat_template.replace("    ", "").replace("\n", "")
        self.template = chat_template

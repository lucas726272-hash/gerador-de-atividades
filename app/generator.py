from __future__ import annotations

import random
from dataclasses import dataclass

from app.models import Difficulty, Grade, Topic, Worksheet


@dataclass(frozen=True)
class TopicContent:
    title: str
    instructions: str
    templates: dict[Difficulty, list[str]]
    challenges: dict[Difficulty, list[str]]


TOPIC_BANK: dict[Topic, TopicContent] = {
    Topic.syllables: TopicContent(
        title="Oficina de Sílabas",
        instructions="Complete as atividades com atenção e leia em voz alta cada palavra.",
        templates={
            Difficulty.easy: [
                "Separe em sílabas: {word}",
                "Circule a sílaba inicial da palavra: {word}",
                "Conte quantas sílabas tem: {word}",
            ],
            Difficulty.medium: [
                "Escreva uma palavra que rime com {word}",
                "Troque a primeira sílaba de {word} por 'pa' e escreva a nova palavra.",
                "Organize as sílabas e forme a palavra: {jumbled}",
            ],
            Difficulty.hard: [
                "Crie uma frase com a palavra {word} e destaque as sílabas tônicas.",
                "Reescreva {word} separando em sílabas e classificando (monossílaba, dissílaba, etc.).",
                "Complete a família silábica usando a sílaba de {word}.",
            ],
        },
        challenges={
            Difficulty.easy: ["Desafio final: escreva 5 palavras da sala e separe todas em sílabas."],
            Difficulty.medium: ["Desafio final: monte um pequeno poema com 4 palavras separadas em sílabas."],
            Difficulty.hard: ["Desafio final: invente 6 palavras e classifique cada uma pelo número de sílabas."],
        },
    ),
    Topic.reading: TopicContent(
        title="Leitura e Compreensão",
        instructions="Leia os textos curtos e responda com frases completas.",
        templates={
            Difficulty.easy: [
                "Leia: 'Lia viu o gato no muro.' Quem Lia viu?",
                "Leia: 'O sol nasceu cedo.' O que aconteceu cedo?",
                "Leia: 'Beto levou suco.' O que Beto levou?",
            ],
            Difficulty.medium: [
                "Leia: 'Ana plantou uma flor e regou à tarde.' O que Ana fez depois de plantar?",
                "Leia: 'Pedro perdeu o lápis, então pediu outro.' Por que Pedro pediu outro lápis?",
                "Leia: 'A turma foi ao pátio porque terminou a tarefa.' Qual foi a causa da ida ao pátio?",
            ],
            Difficulty.hard: [
                "Leia o trecho e escreva a ideia principal: 'No recreio, Clara dividiu seu lanche com João e fez um novo amigo.'",
                "Leia e faça uma inferência: 'As nuvens ficaram escuras e Miguel correu para guardar os brinquedos.' O que provavelmente aconteceu depois?",
                "Reescreva com suas palavras: 'A professora elogiou a turma pela colaboração durante o trabalho em grupo.'",
            ],
        },
        challenges={
            Difficulty.easy: ["Desafio final: leia uma história curta e desenhe a parte que mais gostou, escrevendo uma frase."],
            Difficulty.medium: ["Desafio final: escreva 3 perguntas e respostas sobre um texto que você leu hoje."],
            Difficulty.hard: ["Desafio final: produza um parágrafo resumindo uma fábula conhecida."],
        },
    ),
    Topic.separation: TopicContent(
        title="Separação de Palavras",
        instructions="Observe os espaços entre as palavras e organize as frases corretamente.",
        templates={
            Difficulty.easy: [
                "Separe corretamente: {joined}",
                "Copie a frase colocando espaços: {joined}",
                "Quantas palavras existem em: '{sentence}'?",
            ],
            Difficulty.medium: [
                "Corrija a frase com separação errada: {broken}",
                "Reescreva com separação correta e pontuação: {joined}",
                "Separe e classifique as palavras da frase: {sentence}",
            ],
            Difficulty.hard: [
                "Reescreva o texto separando palavras e justificando duas escolhas: {broken}",
                "Encontre e corrija os erros de separação: {broken}",
                "Crie 2 frases e depois junte as palavras; troque com um colega para separar.",
            ],
        },
        challenges={
            Difficulty.easy: ["Desafio final: separe corretamente 3 frases escritas sem espaço pela professora."],
            Difficulty.medium: ["Desafio final: escreva um bilhete curto e depois marque os limites de cada palavra com cores."],
            Difficulty.hard: ["Desafio final: revise um mini texto de 5 linhas corrigindo separação e pontuação."],
        },
    ),
    Topic.accentuation: TopicContent(
        title="Acentuação Divertida",
        instructions="Leia com atenção e aplique as regras de acentuação estudadas em sala.",
        templates={
            Difficulty.easy: [
                "Coloque acento, se necessário: {word}",
                "Marque a sílaba tônica de: {word}",
                "Escolha a forma correta: {pair}",
            ],
            Difficulty.medium: [
                "Explique por que a palavra '{word}' leva acento.",
                "Complete com acento quando preciso: {sentence}",
                "Classifique {word} em oxítona, paroxítona ou proparoxítona.",
            ],
            Difficulty.hard: [
                "Reescreva o parágrafo aplicando todos os acentos corretamente: {sentence}",
                "Crie 4 palavras acentuadas e diga a regra usada em cada uma.",
                "Encontre o erro de acentuação e corrija: {pair}",
            ],
        },
        challenges={
            Difficulty.easy: ["Desafio final: complete uma cruzadinha com palavras acentuadas."],
            Difficulty.medium: ["Desafio final: escreva 6 palavras e destaque as sílabas tônicas com cores."],
            Difficulty.hard: ["Desafio final: produza um texto curto usando 8 palavras acentuadas corretamente."],
        },
    ),
}

WORDS = ["caderno", "janela", "pipoca", "escola", "amizade", "coração", "árvore", "futebol", "família", "sabiá"]
JOINED = ["omeucadernoénovo", "agataestánajanela", "hojetemsorvete", "vamosbrincarnopatio"]
BROKEN = ["a mi ga foi a pra ça", "ho je va mos ler", "o ga to su biu no te lha do"]
SENTENCES = [
    "A professora leu uma história alegre.",
    "Meu irmão gosta de jogar bola no quintal.",
    "Hoje a turma fez um cartaz colorido.",
]
PAIRS = ["avó / avo", "fácil / facil", "vovô / vovo", "lápis / lapis"]
ILLUSTRATIONS = ["🦉", "📚", "✏️", "🌟", "🧩", "🚌", "🌈", "🐻"]


def _fill_template(template: str, rng: random.Random) -> str:
    word = rng.choice(WORDS)
    return template.format(
        word=word,
        joined=rng.choice(JOINED),
        broken=rng.choice(BROKEN),
        sentence=rng.choice(SENTENCES),
        pair=rng.choice(PAIRS),
        jumbled=" - ".join(rng.sample(list(word), k=min(4, len(word)))),
    )


def generate_worksheet(grade: Grade, topic: Topic, difficulty: Difficulty, seed: int | None = None) -> Worksheet:
    final_seed = seed if seed is not None else random.randint(1, 999_999)
    rng = random.Random(final_seed)

    content = TOPIC_BANK[topic]
    templates = content.templates[difficulty]

    exercises = [_fill_template(rng.choice(templates), rng) for _ in range(10)]
    challenge = rng.choice(content.challenges[difficulty])
    illustrations = rng.sample(ILLUSTRATIONS, k=3)

    return Worksheet(
        title=f"{content.title} - {grade.value}",
        instructions=content.instructions,
        grade=grade,
        topic=topic,
        difficulty=difficulty,
        exercises=exercises,
        final_challenge=challenge,
        illustrations=illustrations,
        seed=final_seed,
    )

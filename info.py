from typing import Dict, List
from google.cloud import firestore
from pydantic import BaseModel

db = firestore.Client(project='gcp-banorte-hackaton-team-13')

class SurveyQuestion(BaseModel):
    question: str
    options: List[str]

class ContentTopic(BaseModel):
    topic: str
    resources: List[str]

class FinancialProduct(BaseModel):
    id: str
    name: str
    description: str

class NewsArticle(BaseModel):
    id: str
    title: str
    content: str

survey_questions_ref = db.collection('survey_questions')
content_topics_ref = db.collection('content_topics')
financial_products_ref = db.collection('financial_products')
news_articles_ref = db.collection('news_articles')

def add_survey_questions(questions: List[SurveyQuestion]):
    """Agregar preguntas de la encuesta a Firestore."""
    for idx, question in enumerate(questions):
        survey_questions_ref.document(f"question_{idx}").set(question.dict())
    print("Preguntas de la encuesta agregadas correctamente.")

def add_content_topics(content_map: Dict[str, Dict[str, List[str]]]):
    """Agregar temas de contenido a Firestore."""
    for topic, content in content_map.items():
        content_topic = ContentTopic(topic=topic, resources=content['resources'])
        content_topics_ref.document(topic).set(content_topic.dict())
    print("Temas de contenido agregados correctamente.")

def add_financial_products(products: List[FinancialProduct]):
    """Agregar productos financieros a Firestore."""
    for product in products:
        financial_products_ref.document(product.id).set(product.dict())
    print("Productos financieros agregados correctamente.")

def add_news_articles(articles: List[NewsArticle]):
    """Agregar artículos de noticias a Firestore."""
    for article in articles:
        news_articles_ref.document(article.id).set(article.dict())
    print("Artículos de noticias agregados correctamente.")

# Datos para preguntas de la encuesta
survey_questions = [
    SurveyQuestion(
        question="¿Conoces los conceptos básicos de finanzas personales?",
        options=["Sí", "No", "Algunos conceptos", "Nunca lo he oído"]
    ),
    SurveyQuestion(
        question="¿Tienes un presupuesto personal?",
        options=["Sí, lo sigo rigurosamente", "Sí, pero no lo sigo", "No, pero planeo tener uno", "No, nunca he tenido"]
    ),
    SurveyQuestion(
        question="¿Conoces la diferencia entre ahorro e inversión?",
        options=["Sí, completamente", "Sí, pero no en profundidad", "He oído hablar de ello", "No tengo idea"]
    ),
    SurveyQuestion(
        question="¿Has invertido alguna vez en acciones o fondos de inversión?",
        options=["Sí, regularmente", "Sí, alguna vez", "No, pero planeo hacerlo", "No, nunca"]
    ),
    SurveyQuestion(
        question="¿Tienes deudas en este momento?",
        options=["Sí, muchas", "Sí, algunas", "No, estoy libre de deudas", "No estoy seguro"]
    ),
    SurveyQuestion(
        question="¿Entiendes cómo funciona el interés compuesto?",
        options=["Sí, lo entiendo bien", "He oído hablar de ello", "No estoy seguro", "No, nunca lo he escuchado"]
    ),
    SurveyQuestion(
        question="¿Sabes cómo mejorar tu score de crédito?",
        options=["Sí, tengo un plan", "He leído sobre ello", "No estoy seguro", "No, no tengo idea"]
    ),
]

# Datos para el diccionario de temas de contenido
content_map = {
    "Conceptos Básicos de Finanzas Personales": {
        "resources": ["Introducción a Finanzas Personales", "Presupuesto Básico", "Ahorro vs. Inversión"]
    },
    "Cómo Crear un Presupuesto": {
        "resources": ["Cómo Crear un Presupuesto", "Control de Gastos", "Herramientas para Presupuesto"]
    },
    "Ahorro vs. Inversión": {
        "resources": ["Introducción a Ahorro", "Tipos de Inversiones", "Riesgo y Rendimiento"]
    },
    "Estrategias de Ahorro": {
        "resources": ["Estrategias de Ahorro", "Ahorro a Largo Plazo", "Inversiones de Bajo Riesgo"]
    },
    "Tipos de Cuentas de Ahorro": {
        "resources": ["Tipos de Cuentas", "Intereses y Beneficios", "Apertura de Cuentas"]
    },
    "Introducción a las Inversiones": {
        "resources": ["Guía de Inversiones", "Riesgo y Rendimiento", "Mercados Financieros"]
    },
    "Gestión de Deudas": {
        "resources": ["Tipos de Deudas", "Estrategias de Pago de Deudas", "Control de Créditos"]
    },
    "Planificación Financiera": {
        "resources": ["Establecimiento de Metas Financieras", "Uso de Herramientas Financieras", "Presupuesto Personal"]
    },
    "Aspectos Fiscales de Inversiones": {
        "resources": ["Declaración de Impuestos", "Beneficios Fiscales", "Planificación Fiscal"]
    },
    "Ética Financiera": {
        "resources": ["Principios de Ética Financiera", "Responsabilidad Financiera", "Sostenibilidad Financiera"]
    }
}

# Datos de productos financieros
financial_products = [
    FinancialProduct(id="prod1", name="Tarjeta de Crédito Banorte", description="Tarjeta de crédito con beneficios."),
    FinancialProduct(id="prod2", name="Cuenta de Ahorro Premium", description="Cuenta de ahorro con altas tasas de interés."),
    FinancialProduct(id="prod3", name="Préstamo Personal Banorte", description="Préstamo personal con tasas competitivas y plazos flexibles."),
    FinancialProduct(id="prod4", name="Seguro de Vida Integral", description="Seguro de vida que ofrece protección y ahorro a largo plazo."),
    FinancialProduct(id="prod5", name="Fondos de Inversión Diversificados", description="Invierte en fondos que se ajustan a tu perfil de riesgo."),
    FinancialProduct(id="prod6", name="Tarjeta de Crédito HSBC", description="Tarjeta de crédito con recompensas y promociones exclusivas."),
    FinancialProduct(id="prod7", name="Cuenta de Ahorro Básica", description="Cuenta de ahorro sin comisiones y fácil acceso a tus fondos.")
]

# Datos de noticias personalizadas
news_articles = [
    NewsArticle(id="news1", title="Noticias sobre inversiones", content="Las mejores oportunidades para invertir."),
    NewsArticle(id="news2", title="Consejos financieros", content="Aprende cómo mejorar tu situación financiera."),
    NewsArticle(id="news3", title="Tendencias del mercado para el próximo trimestre", content="Análisis de las tendencias que afectarán los mercados en los próximos meses."),
    NewsArticle(id="news4", title="Guía práctica para ahorrar más", content="Consejos sencillos para aumentar tus ahorros y alcanzar tus metas financieras."),
    NewsArticle(id="news5", title="Oportunidades en inversiones sostenibles", content="Explora cómo invertir en empresas responsables con el medio ambiente."),
    NewsArticle(id="news6", title="Errores financieros comunes que debes evitar", content="Conoce los errores más comunes en la gestión financiera y cómo evitarlos."),
    NewsArticle(id="news7", title="Nuevas regulaciones financieras y su impacto", content="Entérate de las nuevas regulaciones y cómo pueden afectarte.")
]

# Agregar preguntas de la encuesta, temas de contenido, productos financieros y artículos de noticias a Firestore
add_survey_questions(survey_questions)
add_content_topics(content_map)
add_financial_products(financial_products)
add_news_articles(news_articles)

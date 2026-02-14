import logging

logging.basicConfig(
    filename="gic.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def registrar(mensaje):
    logging.info(mensaje)
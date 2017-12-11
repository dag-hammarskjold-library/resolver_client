from flask import Flask, render_template, request
from logging import getLogger
from sqlalchemy.exc import SQLAlchemyError
from .models import DocumentMetadata
from .db import db_session
from .base_page import BasePage

app = Flask(__name__)
logger = getLogger(__name__)

app.config.from_pyfile('config.py')


def session_commit(session, msg):
    session.flush()
    try:
        session.commit()
    except SQLAlchemyError as e:
        print("Caught Commit error in {}: {}".format(msg, e))
        session.rollback()


@app.errorhandler(404)
def page_not_found(e):
    app.logger.error(e)
    return render_template('404.html'), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        doc_symbols = request.form.get('document_symbols', None)
        symbol_list = []
        if doc_symbols:
            symbols = doc_symbols.split(',')
            symbol_list = [sym.strip() for sym in symbols]
            for elem in symbol_list:
                val = db_session.query(DocumentMetadata).filter_by(document_symbol=elem)
                if not val:
                    metadata_json = _fetch_metadata(val)
                    row = db_session.query(DocumentMetadata).filter_by(document_symbol=val,
                        metadata_json=metadata_json)
                    row.metadata_hash = row._set_hash()
                    db_session.add(row)
                    db_session.commit()
                else:
                    pass

            return render_template('results.html', context=symbol_list)

    else:
        return render_template('index.html')


def _get_column(doc_symbol):
    pass


def _fetch_metadata(document_symbol):
    metadata_url = app.config.get("METDATA_URL")
    page = BasePage()
    root = page.get_root(metadata_url)
    metadata_json = root.xpath('.//pre[@id="document-metadata"]')
    return metadata_json

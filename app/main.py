from app.core.health import health_check
from app.core.logger import get_logger
from app.ui.cli import run_cli

logger = get_logger('anna')

if __name__ == '__main__':
    logger.info('ANNA AI startup check: %s', health_check())
    run_cli()

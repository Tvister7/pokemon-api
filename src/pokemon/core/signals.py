import asyncio
import signal

from structlog import get_logger

logger = get_logger(__name__)


async def shutdown(signal, loop):
    """Cleanup tasks tied to the service's shutdown."""
    try:
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        [task.cancel() for task in tasks]
        await asyncio.gather(*tasks, return_exceptions=True)
        loop.stop()
    except Exception as exc:
        await logger.aerror("shutdown_error", signal=str(signal), exc=str(exc))


async def bind_signals():
    loop = asyncio.get_event_loop()
    signals = (signal.SIGHUP, signal.SIGTERM, signal.SIGINT)
    for s in signals:
        loop.add_signal_handler(s, lambda s=s: asyncio.create_task(shutdown(s, loop)))

import functools
import asyncio
import concurrent

executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

def asyncronize_function(function, *args, **kwargs):
    return asyncio.get_event_loop().run_in_executor(
        executor,
        functools.partial(
            function,
            *args,
            **kwargs
        )
    )
import functools
import asyncio

def asyncronize_function(function, *args, **kwargs):
    return asyncio.get_event_loop().run_in_executor(
        None,
        functools.partial(
            function,
            *args,
            **kwargs
        )
    )
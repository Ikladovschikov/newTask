from aiohttp import web


async def handle(request):
    return web.Response(text='I am working!')

app = web.Application()
app.add_routes(
    [
        web.get('/', handle),
        web.post('/', handle)
    ],
)

if __name__ == '__main__':
    web.run_app(app)

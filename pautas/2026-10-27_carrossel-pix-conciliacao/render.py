import asyncio, glob, os
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width':1080,'height':1350})
        for f in sorted(glob.glob('/home/claude/work/slides/slide-*.html')):
            await pg.goto('file://'+f)
            await pg.evaluate('document.fonts.ready')
            await pg.wait_for_timeout(300)
            out = '/home/claude/work/png/'+os.path.basename(f).replace('.html','.png')
            await pg.screenshot(path=out)
            # overflow check: any element extending beyond canvas or into footer
            r = await pg.evaluate("""()=>{const b=document.querySelector('.body');const f=document.querySelector('.foot');return [b.getBoundingClientRect().bottom, f.getBoundingClientRect().top]}""")
            print(os.path.basename(out), 'body bottom', round(r[0]), 'footer top', round(r[1]))
        await b.close()
asyncio.run(main())

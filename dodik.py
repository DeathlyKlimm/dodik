from .. import loader
from asyncio import sleep
@loader.tds
class DodikMod(loader.Module):
	strings = {"name": "dodik"}
	@loader.owner
	async def dodikcmd(self, message):
		for _ in range(10):
			for dodik in ['хуй', '️сосать', 'не', 'паску', 'грызть', 'соси']:
				await message.edit(dodik)
				await sleep(0.3)
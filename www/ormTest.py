#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio
import orm

from model import User, Blog, Comment

loop = asyncio.get_event_loop()

async def  test():
	await orm.create_pool(loop,user='root', password='pomelo00', db='fuck')

	u = User(name='BBbigdickSucker', email='BBbigpurple@bilibili.com', password='papapa', image='about:blank')

	await u.save()

loop.run_until_complete(test())
loop.close
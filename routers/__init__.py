__all__ = ("router",)

from aiogram import Router

#from .admin_handlers import router as admin_router
from .commands import router as commands_router
from .common import router as common_router
from .media_handlers import router as media_router

router = Router(name=__name__) # Основной роутер будет передан в DSLUbot. в экзэмпляре содержится еще обьекты
                                # Каждый экзмпляр которого  общается со своим пользователем грубо говаря
                                # Уровень общения по качеству, в зависимости от подписки.??
router.include_routers(commands_router)
router.include_routers(media_router)
# this one has to be the last!
router.include_router(common_router) #должен быть в конце потому как если ни кто не подхватил твой, он последний
                                  # кто его обработает!!

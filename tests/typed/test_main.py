from typing import Annotated
from typing import Optional
from typing import Union

# from dynaconf.typed.main import extract_defaults_and_validators_from_typing
from dynaconf.typed.types import DictValue
from dynaconf.typed.types import NotRequired
from dynaconf.typed.validators import Contains


def test_extract():
    class Scheme(DictValue):
        part: str = "http"
        tls: bool = True

    class Link(DictValue):
        url: str = "/1"
        name: str
        scheme: Scheme

    class Profile(DictValue):
        username: str = "um"
        team: int = 66
        avatar: str
        link: Link

    class Person(DictValue):
        name: str = "a"
        port: int
        profile: Profile
        profile2: Profile = {"username": "dois", "link": {"url": "/2"}}
        profile3: Profile = Profile(username="tres", link={"url": "/3"})
        profile4: Annotated[Profile, Contains("name")] = {}
        profile5: NotRequired[Profile] = {"avatar": "123"}
        profile6: Optional[Profile] = {}
        profile7: NotRequired[Profile]
        profiles: list[Profile] = [{"username": "l1"}]
        profiles2: list[Profile] = []
        maybe_profile: Union[Profile, int] = {"port": 199}

    # print("PG", Person.__get_defaults__())

    # defaults, validators = extract_defaults_and_validators_from_typing(Person)
    # print()
    # print(defaults)
    # print(validators)

    # print()
    # p = Person(port=123)
    # for k, v in p.items():
    #     print(k,"=", v)

    # print(p)
    # print(p.profile.link.scheme.part)
    # print(isinstance(p.profile.link, dict))
    # print(p["profile"].link["scheme"]["part"])

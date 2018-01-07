Errbot example plugin
====

# how to use

1. start a docker container

```
docker run -it --rm \
    --name err-text \
    -e BACKEND=Text \
    -e BOT_USERNAME="@testbot" \
    -e BOT_ADMINS="@tkit" \
    -e "TZ=Asia/Tokyo" \
    rroemhild/errbot
```

image : [rroemhild/errbot](https://hub.docker.com/r/rroemhild/errbot/)

2. install this plugin

```
!repos install https://github.com/tkit/errbot-plugin-example
```

here is example:
```
[@tkit ➡ @testbot] >>> !repos install https://github.com/tkit/errbot-plugin-example
[@tkit ➡ @testbot] [␍]
Installing https://github.com/tkit/errbot-plugin-example...
A new plugin repository has been installed correctly from https://github.com/tkit/errbot-plugin-example. Refreshing the plugins commands...
Plugins reloaded.
```


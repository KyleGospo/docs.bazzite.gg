---
title: ScopeBuddy
authors:
  - "@HikariKnight"
tags:
  - Guide
---

## What is?

- A small script that works as a gamescope bridge to avoid having to copy paste long launch options for many games.
- Allows you to set Environment Variables (env vars) and gamescope launch options globally, per game or depending on what mode ScopeBuddy or Steam is running in.
- Gives you the ability to automate running bash scripts before the game runs (this is a side effect of how the config files work)
- You can bring your configurations with you between computers by just copying `~/.config/scopebuddy` to a new device
- It also is used as a workaround to fix the Steam Overlay when using nested gamescope in desktop mode.

## How to use it

**As a `gamescope` replacement just to fix the Steam Overlay**:

If you just want to fix the Steam Overlay (and Steam Input in some games), all you have to do is replace `gamescope` in your launch options for the game with `scb` or `scopebuddy`.
Essentially turning

```bash
XDG_DEFAULT_LAYOUT=no gamescope -w 1920 -h 1080 -W 2560 -H 1440 -- %command% --launcher-skip
```

Into

```bash
XDG_DEFAULT_LAYOUT=no scb -w 1920 -h 1080 -W 2560 -H 1440 -- %command% --launcher-skip
```

Now your Steam Overlay will work when using gamescope for a game in desktop mode! 🎉

## Configuration files

### Setting global defaults

If you ran your game once with the above launch options, scopebuddy will have created a default example config for you `~/.config/scopebuddy/scb.conf`

!!! info "It might be possible that the file doesnt exists, in such case, create an empty one."

Inside the file you can add env vars and setup a default set of gamescope arguments.

```bash
export XDG_DEFAULT_LAYOUT=no
SCB_GAMESCOPE_ARGS="-f -w 2560 -h 1440 -W 2560 -H 1440 -r 180"
```

The above `scb.conf` will make scopebuddy always set the keyboard layout in gamescope to norwegian and run gamescope with the arguments `-f -w 1920 -h 1080 -W 2560 -H 1440 -r 180`

This means we can now shorten our Launch Options for games we want to run in gamescope to just

```bash
scb -- %command% --launcher-skip
```

If you have a different set of defaults you use for a game, for example you want to upscale this game from 1080p to 1440p, then you can have a separate default config and tell scopebuddy to use that instead.
For this example, make the file `1080p.conf` inside `~/.config/scopebuddy/` and add defaults specific to what you want to use for upscaling from 1080p.

```bash
export XDG_DEFAULT_LAYOUT=no
SCB_GAMESCOPE_ARGS="-f -w 1920 -h 1080 -W 2560 -H 1440 -r 180"
```

To use this new config you can tell scopebuddy to use it by setting the `SCB_CONF` env var in the games Launch Option in steam

```bash
SCB_CONF=1080p.conf scb -- %command% --launcher-skip
```

scopebuddy will now use `1080p.conf` instead of `scb.conf` to set default options and environment variables.

!!! note

    If you supply any argument to scopebuddy then `SCB_GAMESCOPE_ARGS` will be ignored entierly!
    This means using the launch option `scb -f -- %command%` will load the env vars from `scb.conf` however it will not use `SCB_GAMESCOPE_ARGS` from any config files.

### Setting specific options for a single Steam game

For this example we will use Path of Exile 2, this game supports HDR, so we want to append the `--hdr-enabled` argument to gamescope.

First we will need to find Path of Exile 2's Steam AppID, you can find this by going to the games **Properties** in Steam and then heading to the **Updates** section.
At the bottom you will see some information, you want the **App ID** value, in our Path of Exile 2 example this is `2694490`.

Now make `2694490.conf` inside `~/.config/scopebuddy/AppID/` and add your Path of Exile 2 specific options.
And for examples sake lets set `ENABLE_GAMESCOPE_WSI` to 0, because lets say it causes issues in this one game for me when it is set to 1 which is default.

```bash
export ENABLE_GAMESCOPE_WSI=0
SCB_GAMESCOPE_ARGS+=" --hdr-enabled"
```

Now when steam runs `scb -- %command%`, scopebuddy will load the config from `scb.conf` then load `AppID/2694490.conf` afterwards to apply extra options on top of the defaults (or replace previous options from the default config if the same variables are exported or changed again)

Notice how `SCB_GAMESCOPE_ARGS` uses `+=` instead of `=`.

- `+=` means append this at the end of the current variable.
- `=` means to replace everything in the variable.

This let's us re-use the `SCB_GAMESCOPE_ARGS` we set in our `scb.conf`

## Frequently asked questions (FAQ)

### Can I use scopebuddys functions without using gamescope?

Yes, just use the env var `SCB_NOSCOPE=1` in the Launch Options like this

```bash
SCB_NOSCOPE=1 scb -- %command% --launcher-skip
```

This will tell scopebuddy to not launch gamescope and ignore `SCB_GAMESCOPE_ARGS` in all configs.
The default config file will also be set to `noscope.conf` instead of `scb.conf` unless you also added the `SCB_CONF` env var to the launch options.

### Does ScopeBuddy work inside Steam Gamemode?

Yes!
When scopebuddy detects that steam is running in gamemode, it will force `SCP_NOSCOPE=1` and `SCB_CONF=gamemode.conf` this means that you can set custom options that will only be used in gamemode while keeping game specific options!

This means you can use scopebuddy to automatically handle using nested gamescope when in desktop mode and not utilizing gamescope when inside gamemode.
No more manually adding and removing gamescope from launch options when you switch between gamemode and desktop mode! 🎉

### Can I have scopebuddy handle the launch options for my games?

Of course! You will just use an AppID config for this and you can then append launch options by adding this to the AppID config for the game.

```bash
command+=" --launcher-skip --some-other-parameter"
```

!!! note

    The `+=` is very important as you NEED to append launch options to the %command%, it is also vital that you start with a space after the first " otherwise the game will fail to launch.

### Wait... This is all just bash!?

Every config file for scopebuddy is a full bash script that is sourced before running gamescope and the game. This means if you are an advanced user you can do some really creative stuff!

Some handy variables available to you are

- `$SCB_NOSCOPE` will be set to 1 if scopebuddy was launched with `SCB_NOSCOPE=1`
- `$SCB_GAMEMODE` will be set to 1 if scopebuddy is ran from within steam gamemode (this also implies `SCB_NOSCOPE=1`)
- `$SCB_CONFIGDIR` will be `$HOME/.config/scopebuddy` this means you can source other configs within your config (please do not make an infinite loop!)
- `$command` will contain the expanded %command% variable from Steam and any launch options you added after it.

Let your creativity go wild!
But please be responsible!

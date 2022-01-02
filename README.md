# UNIX :watch: from NTP

**UNIX time from NTP** or short **UtfN** is a simple CLI tool to set the time from an NTP-Server.

* Sets time and date using the `date` command present in **all UNIX based systems** like **Ubuntu Linux**, **Manjaro** or **FreeBSD**
* **NTP-Server** can be **specified** using a **CLI-argument**
* **Timezone** can be specified using a **CLI-argument**

## Links
* [GitHub](https://github.com/datalexum/UNIX-time-from-NTP)
* [PyPI](https://pypi.org/project/UtfN/)

# How it works

1. UtfN requests the UTC time and date from the default or specified NTP-Server.
2. UtfN calculates local time and date
3. UtfN uses the date command to set the time and date

# Usage

Execute the utfn from command line and add needed arguments.

## Installation

UtfN can be installt from pip (recommandet):

```
python3 -m pip install -U utfn
```

If you want to run the latest version of the code, you can install from git:

```
python3 -m pip install -U git+git://github.com/datalexum/UNIX-time-from-NTP.git
```
## Arguments

| Longform | Shortform |           Description          |      Optional      |    Default   |
|:--------:|:---------:|:------------------------------:|:------------------:|:------------:|
|   help   |     h     | Display help for the arguments | :heavy_check_mark: |     False    |
|  server  |     s     | Provide a specific NTP-Server  | :heavy_check_mark: | pool.ntp.org |
| timezone |     z     | Timezone as a offset from UTC  | :heavy_check_mark: |       0      |

## Errors

There can be two different types of errors.

1. **Connection Error**: It is not possible to connect to the NTP-Server. This can happen if there is no internet connection or the NTP-Server is not available.
2. **Permission Error**: It is not possible to set the date on this system. It is likely that the user has no permission to set the date. Try using a user with higher permissions or add sudo before the command.

## Examples

In the below example utfn is executed with the default NTP-Server and an UTC-offset of 1 to match CET (UTC+1) for the local time in my country.

```
utfn -z 1
```

If everything works as expected the set time is outputed:

```
Time set to 2 JAN 2022 14:32:17
```

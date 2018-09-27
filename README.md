# date format machine - dfm

`dfm --list` to show list of known timestamps and formats.

    key        type                 example                             note                              action
    ---------  -------------------  ----------------------------------  --------------------------------  -------------------
    unix       unix timestamp       1495029745                          seconds since Jan 1 1970          unix_timestamp
    apple      apple timestamp      3577874657                          seconds since Jan 1 1904          apple_timestamp
    microsoft  microsoft timestamp  42872.58630787                      days since Dec 30 1899            microsoft_timestamp
    filetime   filetime             ?                                   100-nanoseconds since Jan 1 1601  filetime_timestamp
    atom       atom                 1975-12-25T14:15:16-05:00                                             pendulum
    cookie     cookie               Thursday, 25-Dec-1975 14:15:16 EST                                    pendulum
    8601       ISO 8601             1975-12-25T14:15:16-0500                                              pendulum
    822        RFC 822              Thu, 25 Dec 75 14:15:16 -0500                                         pendulum
    850        RFC 850              Thursday, 25-Dec-75 14:15:16 EST                                      pendulum
    1036       RFC 1036             Thu, 25 Dec 75 14:15:16 -0500                                         pendulum
    1123       RFC 1123             Thu, 25 Dec 1975 14:15:16 -0500                                       pendulum
    2822       RFC 2822             Thu, 25 Dec 1975 14:15:16 -0500                                       pendulum
    3339       RFC 3339             1975-12-25T14:15:16-05:00                                             pendulum
    rss        rss                  Thu, 25 Dec 1975 14:15:16 -0500                                       pendulum
    w3c        w3c                  1975-12-25T14:15:16-05:00                                             pendulum

Example

    dfm 1496173001 --type unix --out cookie
    Tuesday, 30-May-2017 19:36:41 GMT

    dfm 15:23:45 --out unix
    1513610625


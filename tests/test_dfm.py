"""Tests for date format machine."""
import logging
import pytest           # noqa
import pendulum
from date_format_machine.dfm import DateFormatMachine


log = logging.getLogger()


class TestDFM:
    """Tests for date format machine."""

    def test_unix_timestamp(self):
        """Test unix timestamp."""
        log.debug("test_unix_timestamp")

    def test_milestone_timestamps(self):   # noqa
        """Test milestone timestamp."""
        log.debug("test_milestone_timestamps")
        # http://www.silisoftware.com/tools/date.php
        print("figuring timestamps")
        print("compared to : 2017, 2, 2, 15, 0, 0")

        anchor = pendulum.datetime(2017, 2, 2, 15, 0, 0)
        unix_start = pendulum.datetime(1970, 1, 1, 0, 0, 0)
        apple_start = pendulum.datetime(1904, 1, 1, 0, 0, 0)
        msoft_start = pendulum.datetime(1899, 12, 30, 0, 0, 0)
        file_start = pendulum.datetime(1601, 1, 1, 0, 0, 0)

        udelta = anchor - unix_start
        unix_timestamp = udelta.total_seconds()
        print(f" unix timestamp : {unix_timestamp}")
        assert unix_timestamp == 1486047600

        adelta = anchor - apple_start
        apple_timestamp = adelta.total_seconds()
        print(f"apple timestamp : {apple_timestamp}")
        assert apple_timestamp == 3568892400

        mdelta = anchor - msoft_start
        msoft_timestamp = mdelta.total_days()
        print(f"msoft timestamp : {msoft_timestamp}")
        assert msoft_timestamp == 42768.625000

        fdelta = anchor - file_start
        # filetime_stamp = (fdelta.total_seconds() * 1000000000) / 100
        filetime_stamp = (fdelta.total_seconds() * 10000000)
        print(f" filetime stamp : {filetime_stamp}")
        assert filetime_stamp == 131305212000000000

        apple_diff_unix = unix_start - apple_start
        print(f"apple diff : {apple_diff_unix.total_seconds()}")

        msoft_diff_unix = unix_start - msoft_start
        print(f"msoft diff days : {msoft_diff_unix.total_days()}")
        print(f"msoft diff seconds : {msoft_diff_unix.total_seconds()}")
        file_diff = unix_start - file_start
        print(f" file diff : {file_diff.total_seconds()}")
        file_diff_unix = (131305212000000000 / 10000000) - 11644473600

        print(f" file diff unix : {file_diff_unix}")

    def test_unix_timestamp_parse(self):
        """Test unix timestamp parse."""
        unix = 1486047600
        dfm = DateFormatMachine(unix, 'unix')

        pdt = dfm.parse()
        print(pdt)

        anchor = pendulum.datetime(2017, 2, 2, 15, 0, 0)

        assert pdt == anchor

    def test_apple_timestamp_parse(self):
        """Test apple timestamp parse."""
        apple = 3568892400
        dfm = DateFormatMachine(apple, 'apple')

        pdt = dfm.parse()
        print(pdt)

        anchor = pendulum.datetime(2017, 2, 2, 15, 0, 0)

        assert pdt == anchor

    def test_microsoft_parse(self):
        """Test microsoft parse.

        https://msdn.microsoft.com/en-us/library/office/ff197413.aspx
        """
        microsoft = 42768.852777778
        dfm = DateFormatMachine(microsoft, 'microsoft')

        pdt = dfm.parse()
        print(pdt)

        anchor = pendulum.datetime(2017, 2, 2, 20, 28, 0)

        assert pdt == anchor

        date2 = DateFormatMachine(42768.852777778, 'microsoft').parse()
        print(f"date2 : {date2}")
        assert date2 == anchor

        # m3 = 1.0
        # d3_actual = pendulum.parse('1899-12-31T00:00:00+00:00')
        # d3_test = DateFormatMachine(1.0, 'microsoft')
        # print(f"d3_test {d3_test}")
        # d3_test_parsed = d3_test.parse()
        # print("d3 : %s" % d3_test_parsed)
        # assert d3_test == d3_actual

        # assert m3 == DateFormatMachine.to_microsoft(d3_actual)

        # d4_actual = pendulum.parse('1900-01-01T12:00:00+00:00')
        # d4_test = DateFormatMachine(2.5, 'microsoft').parse()
        # print("d4 : %s" % d4_test)
        # assert d4_test == d4_actual

        date5_actual = pendulum.parse('1992-11-06T03:00:00+00:00')
        date5_test = DateFormatMachine(33914.125, 'microsoft').parse()
        print(f"date5 : {date5_test}")
        assert date5_test == date5_actual

    def test_to_unix(self):
        """Test to unix."""
        date1 = DateFormatMachine('2017-02-02T20:28:25+00:00').parse()
        print(date1)
        date1_unix = DateFormatMachine.to_unix(date1)
        print(date1_unix)
        assert date1_unix == 1486067305

    def test_to_apple(self):
        """Test to apple."""
        date1 = DateFormatMachine('2017-02-02T20:28:25+00:00').parse()
        print(date1)
        date1_apple = DateFormatMachine.to_apple(date1)
        print(date1_apple)
        assert date1_apple == 3568912105

    def test_to_microsoft(self):
        """Test to microsoft.

        Thursday, February 2, 2017 8:28:25pm
        """
        dfm = DateFormatMachine(1486067305, 'unix', 'microsoft')
        date1 = dfm.parse()
        print(date1)
        m_result = DateFormatMachine.to_microsoft(date1)
        print(f"result : {m_result}")

        dfm2 = DateFormatMachine(m_result, 'microsoft', 'cookie')
        date2 = dfm2.parse()
        print(dfm2.report(date2))

        assert date1 == date2

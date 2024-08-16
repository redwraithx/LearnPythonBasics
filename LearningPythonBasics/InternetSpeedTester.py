# install: pip install speedtest-cli
# NOTE: speedtest module will cause an issue, you may need to remove it for this to work. I had to do this, but I did
#       install that by mistake at first.

import speedtest as st


def speed_test():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10 ** 6, 2)

    print("Download Speed in Mbps: ", down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed / 10 ** 6, 2)

    print("Upload Speed in Mbps: ", up_speed)

    ping = test.results.ping
    print("Ping: ", ping)


speed_test()


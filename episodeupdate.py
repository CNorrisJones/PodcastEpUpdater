import argparse
from discord_webhooks import DiscordWebhooks
import feedparser


def webhook_call(url):
    print("Running SHU Episode Update")

    # Pull RSS feed, parse relevant content
    shu_feed = feedparser.parse("http://hoppedupgaming.hipcast.com/rss/super_hopped_up.xml")
    episode_info = shu_feed['entries'][0]
    ep_title = episode_info['title_detail']['value']
    ep_url = episode_info['media_comment']['href']
    ep_description = episode_info['content'][0]['value']

    # Setup content to post, create webhook connection, send post
    discord_content = "New SHU Podcast Episode!\n\n{}\n\n{}\n\n{}".format(ep_title, ep_url, ep_description)
    webhook = DiscordWebhooks(url)
    webhook.set_content(content=discord_content)
    webhook.send()
    print("Episode Update Successful")
    return


def main():
    parser = argparse.ArgumentParser(description="Make Calls to Discord Webhooks")
    parser.add_argument('--web', default=None, type=str, help='Discord Webhook to be used')
    args = parser.parse_args()

    webhook_call(args.web)
    return


if __name__ == "__main__":
    main()

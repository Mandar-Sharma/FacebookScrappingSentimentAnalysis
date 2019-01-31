import facebook


post_id='10154391555365419'
access_token='EAAd7xLnlREoBAEZA7ACoPZBHP88ZApVZB4oKIwZCySXWSOBZCfHoE3WT1nGZAweRNxHZCBuftfBUtYGeg45njV19XNpfvCge4KZB4Ae36gTJFyF6SjbjTzKnfNs6sLByizQV4AehXwrAP5ty6GktQ64BJxtOgSFPd9ZAIZD'
graph = facebook.GraphAPI(access_token)
post = graph.get_object(post_id)

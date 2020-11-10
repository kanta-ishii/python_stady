class User:
    def __init__(self, id: int, displayName: str, userName: str, introduction: str):
        self.id = id
        self.displayName = displayName
        self.userName = userName
        self.introduction = introduction


class Tweet:
    def __init__(self, id: int, user: User, body: str):
        self.id = id
        self.user = user
        self.body = body


#問題1
user1 = User(1,"しんや@東京のアプリ開発会社","@pentagon_tokyo","アプリ開発歴７年目の代表取締役社長")
user2 = User(2, "りーさんIOSエンジニアになるために勉強中", "@iPhone14545061", "iPhoneアプリSwift勉強しています！")
user3 = User(3, "しか", "@KzNtcpYZJvVtj7u", "30歳。このご時世ですが気楽にコツコツと勉強しながらプログラマー目指してます。")
user4 = User(4, "りしん@エンジニアを目指すおじさん", "@Resin311", "福岡在住の４０過ぎた妻子あるおじさんが、転職するためにエンジニアを目指します。")

#問題2
tweet1 = Tweet(1, user1, "家の近くの個人経営のカフェの居心地がよい。最近ここで記事を書いたり。カンタンな作業している。")
tweet2 = Tweet(1, user1, "みんながよく使っているアプリは、開発に1000万円以上かかっているものが多いと思う。")
tweet3 = Tweet(2, user2,"実際にしんやさんのコードを打ってるところを見ると自分もいつかはこのぐらい早く正確にわかりやすくコードを書けるよう")
tweet4 = Tweet(2, user2, "今回の動画で自分が何を勉強すればいいかハッキリわかりました！！")
tweet5 = Tweet(3, user3, "第２回 iOSアプリ開発の全体像。iosエンジニアがアプリビジネスのどの部分を担っているのかがとても分かりやすかったです。")
tweet6 = Tweet(3, user3, "SIerやweb開発の全体像は書籍で見たことあったけど、iosアプリ開発の情報は大変貴重でした。")
tweet7 = Tweet(4, user4, "動画学習第4回\n実務ではあまりstoryboard使わないんですね\n画面遷移するだけでも、知ってるやり方と全然違う…")
tweet8 = Tweet(4, user4, "自分が学ぶべき道筋が、わかるのはありがたいです。")


#問題3
tweet_array = [tweet1, tweet2, tweet3, tweet4, tweet5, tweet6, tweet7, tweet8]

#問題4
app_array = []
for i in range(len(tweet_array)):
    if tweet_array[i].user.displayName.find('アプリ')>=0 or tweet_array[i].user.userName.find('アプリ')>=0 or tweet_array[i].user.introduction.find('アプリ')>=0 or tweet_array[i].body.find('アプリ')>=0:
        app_array.append(tweet_array[i])
    else:
        pass
# print(app_array)

#問題5
app_array_other1 = []
for i in range(len(app_array)):
    if app_array[i].user.id != 1:
        app_array_other1.append(app_array[i])
print(app_array_other1)

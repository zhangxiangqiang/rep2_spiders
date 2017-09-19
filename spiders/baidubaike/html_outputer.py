class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def html_output(self):
        font = open('html_output.html', 'w')
        font.write('<html>')
        font.write('<body>')
        font.write('<table>')
        font.write("<meta charset='utf-8'>")

        for data in self.datas:
            font.write('<tr>')
            font.write("<td>%s</td>" % data['url'].encode('utf-8 '))
            font.write("<td>%s</td>" % data['title'].encode('utf-8 '))
            font.write("<td>%s</td>" % data['summary'].encode('utf-8 '))
            font.write('</tr>')

        font.write('</table>')
        font.write('</body>')
        font.write('</html>')
        font.close()



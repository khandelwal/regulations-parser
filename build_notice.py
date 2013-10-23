from lxml import etree
from regparser.notice.build import process_xml
from regparser.tree.xml_parser import reg_text


def process_notice_xml(notice_xml):
    notice_xml = etree.parse(notice_xml)
    notice = process_xml({
        'cfr_part':'1005', 
        'meta':{'start_page':0}}, 
        notice_xml)
    #print notice['amendments']


def read_notice_xml(notice_xml):
    notice_xml = open(notice_xml, 'r').read()
    notice_tree = reg_text.build_tree(notice_xml)
    print notice_tree

if __name__ == "__main__":
    #notice_xml = '/tmp/2012-1728.xml'
    #notice_xml = '/tmp/2013-06861.xml'
    notice_xml = '/tmp/2013-10604.xml'

    #read_notice_xml(notice_xml)
    process_notice_xml(notice_xml)

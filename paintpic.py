import seaborn as sb
# �ȼ����df��col���е�ֵ�ĳ��ִ������ٻ�����״ͼ
sb.countplot(df['col']
#ɢ��ͼ
sb.jointplot(x='col1',y='col2',data=df)
# ֱ��ͼ
sb.distplot(df['col'], bins=10)

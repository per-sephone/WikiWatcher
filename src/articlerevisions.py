class ArticleRevisions:

    def __init__(self, titles) -> None:
        """ REMOVE THIS ON MERGE """
        pass
        
    def format_timestamp(self, year, month, day, hour, minute, second):
        if year:
            ret = str(year)
        else:
            raise Exception #TODO
        ret += str(month).rjust(2, "0") if month else "01"
        ret += str(day).rjust(2, "0") if day else "01"
        ret += str(hour).rjust(2, "0") if hour else "00"
        ret += str(minute).rjust(2, "0") if minute else "00"
        ret += str(second).rjust(2, "0") if second else "01"
        return ret

if __name__ == "__main__":
    a = ArticleRevisions()
    print('20080607040130')
    print(a.format_timestamp(2008, 6, 7, 4, 1, 30))
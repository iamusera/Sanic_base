class ViewResult:
    def __init__(self, message, data):
        self.result_dic = dict()
        self.result_dic['message'] = message
        self.result_dic['data'] = data

    def result(self):
        return self.result_dic


class SuccessResult(ViewResult):
    def __init__(self, message, data):
        super(SuccessResult, self).__init__(message, data)
        self.result_dic['code'] = 200
        self.result_dic['success'] = True


class FailureResult(ViewResult):
    def __init__(self, message, data='', exception=''):
        super(FailureResult, self).__init__(message, data)
        self.result_dic['code'] = 500
        self.result_dic['success'] = False
        self.result_dic['exception'] = exception



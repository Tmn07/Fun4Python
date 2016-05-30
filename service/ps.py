import win32serviceutil   
import win32service   
import win32event   
  
class PythonService(win32serviceutil.ServiceFramework):   
    """ 
    Usage: 'PythonService.py [options] install|update|remove|start [...]|stop|restart [...]|debug [...]' 
    Options for 'install' and 'update' commands only: 
     --username domain\username : The Username the service is to run under 
     --password password : The password for the username 
     --startup [manual|auto|disabled|delayed] : How the service starts, default = manual 
     --interactive : Allow the service to interact with the desktop. 
     --perfmonini file: .ini file to use for registering performance monitor data 
     --perfmondll file: .dll file to use when querying the service for 
       performance data, default = perfmondata.dll 
    Options for 'start' and 'stop' commands only: 
     --wait seconds: Wait for the service to actually start or stop. 
                     If you specify --wait with the 'stop' option, the service 
                     and all dependent services will be stopped, each waiting 
                     the specified period. 
    """  

    _svc_name_ = "PythonService"  

    _svc_display_name_ = "Python Service Demo"  

    _svc_description_ = "Python service demo."  
  
    def __init__(self, args):   
        win32serviceutil.ServiceFramework.__init__(self, args)   
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  
        self.logger = self._getLogger()  
        self.isAlive = True  
          
    def _getLogger(self):  
        import logging  
        import os  
        import inspect  
          
        logger = logging.getLogger('[PythonService]')  
          
        this_file = inspect.getfile(inspect.currentframe())  
        dirpath = os.path.abspath(os.path.dirname(this_file))  
        handler = logging.FileHandler(os.path.join(dirpath, "service.log"))  
          
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')  
        handler.setFormatter(formatter)  
          
        logger.addHandler(handler)  
        logger.setLevel(logging.INFO)  
          
        return logger  
  
    def SvcDoRun(self):  
        import time  
        self.logger.error("svc do run....")   
        t = 0
        while self.isAlive:  
            self.logger.error("having start "+str(t)+"s")  
            t+=1
            time.sleep(1)  

        #win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)   
              
    def SvcStop(self):   

        self.logger.error("svc do stop....")  
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)   

        win32event.SetEvent(self.hWaitStop)   
        self.isAlive = False  
  
if __name__=='__main__':   
    win32serviceutil.HandleCommandLine(PythonService)  
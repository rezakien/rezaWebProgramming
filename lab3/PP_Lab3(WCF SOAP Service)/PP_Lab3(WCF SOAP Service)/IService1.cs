using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using System.Data;

namespace PP_Lab3_WCF_SOAP_Service_
{
    [ServiceContract]
    public interface IService1
    {
        [OperationContract]
        DataSet getClients(string ID_Client = null);
        [OperationContract]
        string postClients(string Name);
        [OperationContract]
        string putClients(int ID_Client,string Name);
        [OperationContract]
        string deleteClients(int ID_Client);

        [OperationContract]
        DataSet getService(string ID_Service = null);
        [OperationContract]
        string postService(string ServiceName,float ServicePrice);
        [OperationContract]
        string putService(int ID_Service, string ServiceName,float ServicePrice);
        [OperationContract]
        string deleteService(int ID_Service);

        [OperationContract]
        DataSet getOrders(string ID_Order = null);
        [OperationContract]
        string postOrders(DateTime OrderDate,int Client_ID);
        [OperationContract]
        string putOrders(int ID_Order, DateTime OrderDate, int Client_ID);
        [OperationContract]
        string deleteOrders(int ID_Order);

        [OperationContract]
        DataSet getOS(string ID_OS = null);
        [OperationContract]
        string postOS(int Order_ID,int Service_ID, int Quentity);
        [OperationContract]
        string putOS(int ID_OS, int Order_ID, int Service_ID, int Quentity);
        [OperationContract]
        string deleteOS(int ID_OS);
    }
}

using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Sql;
using System.Data.SqlClient;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
namespace PP_Lab3_WCF_SOAP_Service_
{
    // ПРИМЕЧАНИЕ. Команду "Переименовать" в меню "Рефакторинг" можно использовать для одновременного изменения имени класса "Service1" в коде, SVC-файле и файле конфигурации.
    // ПРИМЕЧАНИЕ. Чтобы запустить клиент проверки WCF для тестирования службы, выберите элементы Service1.svc или Service1.svc.cs в обозревателе решений и начните отладку.
    public class Service1 : IService1
    {
        string conSct = "Data Source=DESKTOP-LJVB48K;Initial Catalog=PP_Lab3;Integrated Security=True";
        
        public string deleteClients(int ID_Client)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "deleteClient";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@ID_Client", ID_Client);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Запись удалена";
            }
        }

        public string deleteOrders(int ID_Order)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "deleteOrder";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@ID_Order", ID_Order);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Запись удалена";
            }
        }

        public string deleteOS(int ID_OS)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "deleteOS";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@ID_OS", ID_OS);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Запись удалена";
            }
        }

        public string deleteService(int ID_Service)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "deleteService";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@ID_Service", ID_Service);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Запись удалена";
            }
        }

        public DataSet getClients(string ID_Client = null)
        {
            using(SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "getClients";
                SqlCommand cmd = new SqlCommand(proc,con);
                cmd.CommandType = CommandType.StoredProcedure;
                if (ID_Client != null)
                {
                    cmd.Parameters.AddWithValue("@ID_Client", ID_Client);
                }
                cmd.Connection.Open();
                DataSet ds = new DataSet();
                DataTable table = new DataTable();
                table.Load(cmd.ExecuteReader());
                ds.Tables.Add(table);
                cmd.Connection.Close();
                return ds;
            }
        }

        public DataSet getOrders(string ID_Order = null)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "getOrders";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                if (ID_Order != null)
                {
                    cmd.Parameters.AddWithValue("@ID_Order", ID_Order);
                }
                cmd.Connection.Open();
                DataSet ds = new DataSet();
                DataTable table = new DataTable();
                table.Load(cmd.ExecuteReader());
                ds.Tables.Add(table);
                cmd.Connection.Close();
                return ds;
            }
        }

        public DataSet getOS(string ID_OS = null)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "getOS";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                if (ID_OS != null)
                {
                    cmd.Parameters.AddWithValue("@ID_OS", ID_OS);
                }
                cmd.Connection.Open();
                DataSet ds = new DataSet();
                DataTable table = new DataTable();
                table.Load(cmd.ExecuteReader());
                ds.Tables.Add(table);
                cmd.Connection.Close();
                return ds;
            }
        }

        public DataSet getService(string ID_Service = null)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "getServices";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                if (ID_Service != null)
                {
                    cmd.Parameters.AddWithValue("@ID_Service", ID_Service);
                }
                cmd.Connection.Open();
                DataSet ds = new DataSet();
                DataTable table = new DataTable();
                table.Load(cmd.ExecuteReader());
                ds.Tables.Add(table);
                cmd.Connection.Close();
                return ds;
            }
        }

        public string postClients(string Name)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "addClient";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@Name", Name);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Добавлена новая запись в таблицу Clients: Name - " + Name;
            }
        }

        public string postOrders(DateTime OrderDate, int Client_ID)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "addOrder";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@DateOrder", OrderDate);
                cmd.Parameters.AddWithValue("@Client_ID", Client_ID);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Добавлена новая запись в таблицу Orders: OrderDate - " + OrderDate + " Client_ID - " + Client_ID;
            }
        }

        public string postOS(int Order_ID, int Service_ID, int Quentity)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "addOS";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@Order_ID", Order_ID);
                cmd.Parameters.AddWithValue("@Service_ID", Service_ID);
                cmd.Parameters.AddWithValue("@Quentity", Quentity);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Добавлена новая запись в таблицу OrdersServices: Order_ID - " + Order_ID + " Service_ID - "+ Service_ID + " Quentity - " + Quentity;
            }
        }

        public string postService(string ServiceName, float ServicePrice)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "addService";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@ServiceName", ServiceName);
                cmd.Parameters.AddWithValue("@Price", ServicePrice);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                return "Добавлена новая запись в таблицу Services: ServiceName - " + ServiceName + " ServicePrice - " + ServicePrice;
            }
        }

        public string putClients(int ID_Client, string Name)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "updateClient";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@Name", Name);
                cmd.Parameters.AddWithValue("@ID_Client", ID_Client);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Запись обновлена";
            }
        }

        public string putOrders(int ID_Order, DateTime OrderDate, int Client_ID)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "updateOrder";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@ID_Order", ID_Order);
                cmd.Parameters.AddWithValue("@DateOrder", OrderDate);
                cmd.Parameters.AddWithValue("@Client_ID", Client_ID);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Запись обновлена";
            }
        }

        public string putOS(int ID_OS, int Order_ID, int Service_ID, int Quentity)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "updateOS";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@ID_OS", ID_OS);
                cmd.Parameters.AddWithValue("@Order_ID", Order_ID);
                cmd.Parameters.AddWithValue("@Service_ID", Service_ID);
                cmd.Parameters.AddWithValue("@Quentity", Quentity);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Запись обновлена";
            }
        }

        public string putService(int ID_Service, string ServiceName, float ServicePrice)
        {
            using (SqlConnection con = new SqlConnection(conSct))
            {
                string proc = "updateService";
                SqlCommand cmd = new SqlCommand(proc, con);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddWithValue("@ID_Service", ID_Service);
                cmd.Parameters.AddWithValue("@ServiceName", ServiceName);
                cmd.Parameters.AddWithValue("@ServicePrice", ServicePrice);
                cmd.Connection.Open();
                var res = cmd.ExecuteNonQuery();
                cmd.Connection.Close();
                return "Запись обновлена";
            }
        }
    }
}

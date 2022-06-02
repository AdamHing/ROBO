using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.IO;
using System.Diagnostics;
using Microsoft.Win32;




namespace Roblox_Bot_GUI
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            string dir = System.IO.Directory.GetCurrentDirectory();
            Console.WriteLine("testing");
            Console.WriteLine(dir);
        }
        
        
       
        /// runing the bots
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            
            ///path to .xlsx list of bot accounts
            string listpath = TextBox1.Text;
            MessageBox.Show(listpath);

            ///make a thing for randomly generating names too

            ///url of leader account
            string leader_url = TextBox2.Text;
            MessageBox.Show(leader_url);

            /// the amount of bots to be activated
            string NumOfBots = TextBox3.Text;
            MessageBox.Show(NumOfBots);

            

            ///Current working directory
            string CWD = Directory.GetCurrentDirectory();
            MessageBox.Show(CWD);

            /// Write to file for python
           /* using (StreamWriter writer = new StreamWriter("D:/Wfile.txt"))
            {
                writer.WriteLine(listpath);
                writer.WriteLine(leader_url);
               
            }*/


            string arguments = ' ' + listpath + ' ' + leader_url + ' ' + NumOfBots;
            ///Runs 
            string fileName = @"RobloxBots\Package\cstest.py" + arguments;

            Process p = new Process();
            p.StartInfo = new ProcessStartInfo(@"python", fileName)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            p.Start();

            string output = p.StandardOutput.ReadToEnd();
            p.WaitForExit();

            Console.WriteLine(output);

            Console.ReadLine();

        }

        private void btnOpenFile_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            if (openFileDialog.ShowDialog() == true)
                TextBox1.Text = openFileDialog.FileName;
        }

        private void Make_Button_Click(object sender, RoutedEventArgs e)
        {

            Process p;
            string output;
            string RunMakeBotList;
            string fileName;

            /// password for all accounts
            string passwordMaker = PasswordBoxm.Password.ToString();
            MessageBox.Show(passwordMaker);

            /// Url of leader account to friend
            string leadersURLm = TextBox3m.Text;

            /// amount of bots to make
            string NumOfBotsToMake = TextBox4m.Text;


            ///  list of bots in tab 1
            string PremadeBotlist = TextBox1m.Text;


            Console.WriteLine(File.Exists(PremadeBotlist));

            string arguments = ' ' + PremadeBotlist + ' ' + passwordMaker + ' ' + leadersURLm + ' ' + NumOfBotsToMake;

            if (String.IsNullOrEmpty(PremadeBotlist))
            {
                if (MessageBox.Show("No list found. Would you like to make one?", "Question", MessageBoxButton.YesNo, MessageBoxImage.Information) == MessageBoxResult.No)
                {
                    ///do no stuff
                    
                }
                else if (File.Exists(PremadeBotlist) == false)
                {
                    MessageBox.Show("that does not exist");
                }
                else
                {
                    ///do yes stuff
                    ///Runs python code for making the list of bots
                    RunMakeBotList = @"ROBLOXBOTS\Package\BotMaker\generate bot list";///this has not been made yet

                    p = new Process();
                    p.StartInfo = new ProcessStartInfo(@"python", RunMakeBotList)
                    {
                        RedirectStandardOutput = true,
                        UseShellExecute = false,
                        CreateNoWindow = true
                    };
                    p.Start();

                    output = p.StandardOutput.ReadToEnd();
                    p.WaitForExit();

                    Console.WriteLine(output);
                }
            }
            else
            {
                ///Runs python code for Making the bot accounts
                fileName = @"D:\coding\python\RobloxAFKBots\cstest.py" + arguments;

                ///please send help.
                p = new Process();
                p.StartInfo = new ProcessStartInfo(@"C:/ProgramData/Anaconda3/python.exe", fileName)
                {
                    RedirectStandardOutput = true,
                    UseShellExecute = false,
                    CreateNoWindow = true
                };
                p.Start();

                output = p.StandardOutput.ReadToEnd();
                p.WaitForExit();

                Console.WriteLine(output);

                Console.ReadLine();
            }
        }
        private void btnOpenFile_Clicktab1(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            if (openFileDialog.ShowDialog() == true)
                TextBox1m.Text = openFileDialog.FileName;
        }
        /* private void run_cmd()
         {



         }*/


    }
}

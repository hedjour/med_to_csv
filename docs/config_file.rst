Config file yaml
=================

Set up
---------------

The config file is a necessary file that gives the setup of your data for the software.
You can find an example in the config.yml file which contains all possibilities of setup. 
Med-PC can create different types of files:

#. One-column file, where the data is represented in only one column, and 
#. Annotated file, where the data is labelled by the letters from the Med-Associate script

.. note:: You can mix directories of one-column files and directories of annotated files in one folder.

#. There are three types of parameters:

   * info_col : One column file
   * info_lab : labelled file
   * options : further options


   .. important:: Either info_col or info_lab are required, if your data contains a mix 
       of one-column files and labelled files you can mention both parameters 
       
#. For the first two types of parameters (info_col or info_lab):
   
   You need to indicate the information in this format: "Key : Value"
    
   * Keys are the column names that you want in the output file
   * Values are:

     * for infos_col: row number - 1 (Python starts index at 0)
     * for infos_lab: letters used in medAssociate exercise

#. Options:

   * remove_zero_ending : True or False to keep or remove Zeros at the end of arrays. In the Med-PC language, the number of slots in an array is defined by the user. If the number of value is < number of slot, then MedPC will add 0 for missing values. If you do not want these data in your csv file, specify the option True in your yaml file.
   * filter : a string present in the directories name present in the file directories name that you want to use to select a subgroup of datafiles or directories. For example, you can name test session with the string “test” and use it to filter data excluding data that does not contain the string “test” in their name.
   * cut : Some users “tag” data in an array in “TimeStamp.CodeEvent”. For example, they can add a decimal to the time stamp of the event to indicate a specific condition. These data can be retrieved in two separate columns using this option. The value must be a list of list of 4 elements :

     * key to cut
     * separator: usually the dot character
     * column name of first part (eg: TimeStamp)
     * column name of second part (eg: CodeEvent)
     * eval : for some columns the values must be the result of a Python command line (e.g to get information in a path). This must be a python dictionary with Key (column name) and value (short command in a string format).

#. The following Keys are med associate keywords only usable with labelled file :

   * Start Date (automatically added)
   * End Date
   * Subject
   * Experiment
   * Group
   * Box
   * Start Time (automatically added)
   * End Time
   * MSN: Medassociate exercice names

.. note:: Templates are available in the config.yml file or see below

Templates 
----------

.. code-block:: yaml

    infos_col:
        subject: 6
        box: 9
        delay: 66
        step_at_endsess: 73
        sk_dur_at_endsess: 88
        reinforced_resp: 90
        reinforcers: 91
        res_during_reward_deliv: 92
        to_resp: 93
        delivery_s: 94
        to_s: 95
        shock_s: 96
        resets_number: 97
        reinforcers_max_sk_dur: 98
        mn_left_non_resp: 99
        resp_cur_sk_dur: 100
        final_sk_dur: 101
        base_value: [120,"end"]

    infos_lab:
        subject: "Subject"
        box: "Box"
        delay: "B"
        step_at_endsess: "I"
        sk_dur_at_endsess: "X"
        reinforced_resp: ["Z", 0]
        reinforcers: ["Z", 1]
        res_during_reward_deliv: ["Z", 2]
        to_resp: ["Z", 3]
        delivery_s: ["Z", 4]
        to_s: ["Z", 5]
        shock_s: ["Z", 6]
        resets_number: ["Z", 7]
        reinforcers_max_sk_dur: ["Z", 8]
        mn_left_non_resp: ["Z", 9]
        resp_cur_sk_dur: ["Z", 10]
        final_sk_dur: ["Z", 11]
        base_value: ["Z", 30, "end"]

    options:
        remove_zero_ending: True #Or False
        #https://docs.python.org/3/howto/regex.html
        filter: "shock"
        cut : [["base_value", ".", "time_stamp", "shock_step"]]
        eval: {"prog":"path_file.split('/')[-1]"}

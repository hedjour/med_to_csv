Config file yaml
=================

Introduction to setting :
-------------------------

The config file is a necessary file that gives the setup of your data to the soft.
You can find as an example the config.yml which contains all possibilities of setup.
You can mixe 1 col file dir and labelled dir file in experiment dir.

#. There are three types of parameters:

   * info_col : One column file
   * info_lab : labelled file
   * options : further options


   .. important:: The options parameters is required

#. For the first two types of parameters.
    You need to indicate the information in this format: "Key : Value"

    * Keys are the column names that you want in the output file
    * Values are:

      * for infos_col: row number - 1 (Start index :0)
      * for infos_lab: letters used in medAssociate exercise
      * for infos_opt: (see next point)

#. Options:

   * remove_zero_ending : True or False to keep or remove Zeros at the end of arrays
   * Cut : for cutting an output on a special character usually a dot into 2 columns. The value must be a list of list of 4 elements :

     * key to cut
     * separator usually the dot character
     * Col names of first sub-element
     * Col names of second sub-element
   * Eval : for some columns the values must be the result of a Python command line (e.g to get information in a path). It's necessarly a python dictionary with Key as column name and value a short command line as a string.

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

Templates :
------------

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

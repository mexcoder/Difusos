from tkinter import ttk
import tkinter as tk
from ..networks.networkRule import NetworkRule
import sys

class RuleConfigPanel(ttk.Frame):

    def __init__(self, rule: NetworkRule, *args, ruleName=None, callback=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.externaCallback = callback
        self.rule=rule

        proplist = rule.getProperties()
        className = rule.__class__.__name__ 
        if ruleName is None:
            sequential = "" if "seq" not in kwargs else kwargs["seq"]
            ruleName = className+ " " + sequential

        for name, prop in proplist:
            ttk.Label(self, text = name).pack()
            var = tk.DoubleVar(value=getattr(rule,name), name="{}-{}-{}".format(className, hash(rule), name))
            
            tk.Spinbox(self,
                    bg='white',
                    increment=0.1,
                    justify=tk.CENTER,
                    # width=8,
                    from_=sys.float_info.max * -1,
                    to=sys.float_info.max,
                    wrap=False,
                    insertwidth=1,
                    textvariable=var).pack(anchor=tk.CENTER) 
            var.trace("w", lambda *args, name=name, prop=prop, var=var:
                         self.callback(name, prop, var, *args))
            
        self.pack()

    def callback(self, propName, prop, variable, *args, **kwargs):
        setattr(self.rule, propName, variable.get())
        if self.externaCallback is not None:
            self.externaCallback()

    
                 CalculatorToolkit
                        │
            ┌───────────┼───────────┐
            │           │           │
           add       subtract    multiply
            │           │           │
            └───────────┼───────────┘
                        │
                     divide
                        │
                        ▼
                   get_tools()
                        │
                        ▼
                 [Tool objects]
                        │
                        ▼
                 llm.bind_tools()
                        │
                        ▼
                     Gemini
                        │
          "Calculate 20 multiplied by 5"
                        │
                        ▼
             tool_call: multiply
                  a=20, b=5
                        │
                        ▼
               multiply.invoke()
                        │
                        ▼
                      100.0
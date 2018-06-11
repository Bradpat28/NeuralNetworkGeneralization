//
//  ViewController.h
//  NNRunViewer
//
//  Created by Brad Patterson on 10/11/17.
//  Copyright © 2017 Brad Patterson. All rights reserved.
//

#import <Cocoa/Cocoa.h>

@interface ViewController : NSViewController

@property (weak) IBOutlet NSButton *classifyPhotos;
@property (weak) IBOutlet NSButton *startNN;
@property (weak) IBOutlet NSPathControl *projectWorkspace;
@property (weak) IBOutlet NSButton *visAllNN;
@property (weak) IBOutlet NSComboBox *nnRunStats;
@property (weak) IBOutlet NSComboBox *nnRunner;
@property (weak) IBOutlet NSTextField *valPerStat;
@property (weak) IBOutlet NSTextField *numEpochStat;
@property (weak) IBOutlet NSTextField *valAccStat;
@property (weak) IBOutlet NSTextField *testAccStat;
@property (weak) IBOutlet NSTextField *numValImgStat;
@property (weak) IBOutlet NSTextField *numTrainImgStat;
@property (weak) IBOutlet NSTextField *totalTrainTimeStat;
@property (weak) IBOutlet NSTextField *valPercentUser;
@property (weak) IBOutlet NSTextField *numEpochsUser;
@property (weak) IBOutlet NSTextField *stepsEpochUser;
@property (weak) IBOutlet NSTextField *valStepsUser;
@property (weak) IBOutlet NSTextFieldCell *userReportTextField;
@property (weak) IBOutlet NSTextField *batchSizeUser;

#define TOTAL_TIME_IDENT @"S'totalTime'"
#define NUM_TRAIN_IMG_IDENT @"sS'numTrainImg'"
#define NUM_VAL_IMG_IDENT @"sS'numValImg'"
#define NUM_EPOCH_IDENT @"sS'numEpochs'"
#define VAL_IMG_PERCENT_IDENT @"sS'valImgPercent'"
#define LAST_VAL_PERCENT_IDENT @"sS'lastValPercent'"
#define LAST_TRAIN_PERCENT_IDENT @"sbasS'lastTrainPercent'"


@end

